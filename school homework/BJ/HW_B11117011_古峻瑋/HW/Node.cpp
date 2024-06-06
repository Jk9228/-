#include "node.h"
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <algorithm>

node::node(int id, double x, double y, double speedX, double speedY, double accelX, double accelY, const string& color)
    : id(id), x(x), y(y), speedX(speedX), speedY(speedY), accelX(accelX), accelY(accelY), color(color) {}

double node::distance(const node& a, const node& b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

node node::generateRandnode(int id, double L, double W) {
    double x = static_cast<double>(rand()) / RAND_MAX * L;
    double y = static_cast<double>(rand()) / RAND_MAX * W;
    double speedX = static_cast<double>(rand()) / RAND_MAX * 10; // Speed in X direction between 0 and 10
    double speedY = static_cast<double>(rand()) / RAND_MAX * 10; // Speed in Y direction between 0 and 10
    double accelX = static_cast<double>(rand()) / RAND_MAX * 2 - 1; // Acceleration in X direction between -1 and 1
    double accelY = static_cast<double>(rand()) / RAND_MAX * 2 - 1; // Acceleration in Y direction between -1 and 1

    // 隨機生成顏色
    string colors[] = {"黑色", "灰色", "藍色"};
    string color = colors[rand() % 3];

    return node(id, x, y, speedX, speedY, accelX, accelY, color);
}

void node::update(double timeInterval) {
    // 更新速度
    speedX += accelX * timeInterval;
    speedY += accelY * timeInterval;
    // 更新位置
    x += speedX * timeInterval;
    y += speedY * timeInterval;
}

area::area(double L, double W, int N) : L(L), W(W) {
    for (int i = 0; i < N; ++i) {
        nodes.push_back(node::generateRandnode(i, L, W));
    }
}

void area::findDistance() {
    if (nodes.size() < 2) return;

    double minDist = numeric_limits<double>::max();
    double maxDist = 0.0;
    node* minNodeA = nullptr;
    node* minNodeB = nullptr;
    node* maxNodeA = nullptr;
    node* maxNodeB = nullptr;

    for (size_t i = 0; i < nodes.size(); ++i) {
        for (size_t j = i + 1; j < nodes.size(); ++j) {
            double dist = node::distance(nodes[i], nodes[j]);
            if (dist < minDist) {
                minDist = dist;
                minNodeA = &nodes[i];
                minNodeB = &nodes[j];
            }
            if (dist > maxDist) {
                maxDist = dist;
                maxNodeA = &nodes[i];
                maxNodeB = &nodes[j];
            }
        }
    }

    cout << "最小距離: " << minDist << " 在節點 " << minNodeA->id << " 和節點 " << minNodeB->id << " 之間\n";
    cout << "最大距離: " << maxDist << " 在節點 " << maxNodeA->id << " 和節點 " << maxNodeB->id << " 之間\n";
}

void area::printNodes() {
    for (const auto& node : nodes) {
        cout << "節點 ID: " << node.id << " 位置: (" << node.x << ", " << node.y << ") 速度: (" << node.speedX << ", " << node.speedY << ") 加速度: (" << node.accelX << ", " << node.accelY << ") 顏色: " << node.color << "\n";
    }
}

void area::updateNodes(double timeInterval) {
    for (auto& node : nodes) {
        node.update(timeInterval);
    }
}
