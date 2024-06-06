#include <iostream>
#include <cstdlib>
#include <ctime>
#include <Windows.h>
#include "MMSystem.h"
#include "Node.h"
#include "main.h"
using namespace std;

void playSound() {
    // 修改成新的音檔路徑
    PlaySound(TEXT("newyareyare.wav"), NULL, SND_SYNC);
    cout << "播放聲音...\n";
}


void initialObj() {
    // 初始化三個節點
    node node1 = node::generateRandnode(1, 1000, 1000);
    node node2 = node::generateRandnode(2, 1000, 1000);
    node node3 = node::generateRandnode(3, 1000, 1000);

    cout << "初始化節點 1: (" << node1.x << ", " << node1.y << "), 速度: (" << node1.speedX << ", " << node1.speedY << "), 加速度: (" << node1.accelX << ", " << node1.accelY << "), 顏色: " << node1.color << "\n";
    cout << "初始化節點 2: (" << node2.x << ", " << node2.y << "), 速度: (" << node2.speedX << ", " << node2.speedY << "), 加速度: (" << node2.accelX << ", " << node2.accelY << "), 顏色: " << node2.color << "\n";
    cout << "初始化節點 3: (" << node3.x << ", " << node3.y << "), 速度: (" << node3.speedX << ", " << node3.speedY << "), 加速度: (" << node3.accelX << ", " << node3.accelY << "), 顏色: " << node3.color << "\n";
}

int main() {
    srand(static_cast<unsigned>(time(0)));

    double L, W;
    int N;
    double timeInterval = 1.0; // 假設時間間隔為1秒

    cout << "請輸入長度 L: ";
    cin >> L;
    cout << "請輸入寬度 W: ";
    cin >> W;
    cout << "請輸入節點數量 N: ";
    cin >> N;

    // 播放聲音
    playSound();

    area a(L, W, N);
    a.printNodes();
    a.findDistance();

    initialObj();

    a.updateNodes(timeInterval);
    cout << "更新後的節點位置:\n";
    a.printNodes();

    return 0;
}
