#ifndef NODE_H
#define NODE_H

#include <vector>
#include <string>
using namespace std;

class node {
public:
    int id;
    double x, y;
    double speedX, speedY;  // 分別代表X和Y方向的速度
    double accelX, accelY;  // 分別代表X和Y方向的加速度
    string color;           // 顏色屬性

    node(int id, double x, double y, double speedX, double speedY, double accelX, double accelY, const string& color);
    static double distance(const node& a, const node& b);
    static node generateRandnode(int id, double L, double W);
    void update(double timeInterval); // 根據時間間隔更新節點位置
};

class area {
public:
    double L, W;
    vector<node> nodes;

    area(double L, double W, int N);
    void findDistance();
    void printNodes();
    void updateNodes(double timeInterval); // 更新所有節點的位置
};

#endif // NODE_H
