#!/usr/bin/python3

import random
import sys

class MinHeap:
    def __init__(self):
        self.data = []

    def getSize(self):
        return len(self.data)

    def reBuildingWhenPush(self):
        idx = self.getSize() - 1

        while idx > 0:
            parent = int((idx - 1) / 2)
            left = parent * 2 + 1
            right = parent * 2 + 2

            # Have only left child
            if self.getSize() <= right:
                if self.data[parent] > self.data[left]:
                    self.data[parent], self.data[left] = self.data[left], self.data[parent]

                idx = parent
                continue

            if self.data[left] < self.data[parent] and self.data[left] < self.data[right]:
                self.data[parent], self.data[left] = self.data[left], self.data[parent]
            elif self.data[right] < self.data[parent] and self.data[right] < self.data[left]:
                self.data[parent], self.data[right] = self.data[right], self.data[parent]

            idx = parent

    def reBuildingWhenPop(self):
        idx = 0

        while idx < self.getSize() - 1:
            left = idx * 2 + 1
            right = idx * 2 + 2

            if self.getSize() <= left:
                break

            # Have only left child
            if self.getSize() <= right:
                if self.data[idx] > self.data[left]:
                    self.data[idx], self.data[left] = self.data[left], self.data[idx]

                idx = left
                continue

            if self.data[left] < self.data[idx] and self.data[left] < self.data[right]:
                self.data[idx], self.data[left] = self.data[left], self.data[idx]
                idx = left
            elif self.data[right] < self.data[idx] and self.data[right] < self.data[left]:
                self.data[idx], self.data[right] = self.data[right], self.data[idx]
                idx = right
            else:
                break

    def push(self, value):
        self.data.append(value)
        self.reBuildingWhenPush()

    def pop(self):
        if self.getSize() == 0:
            return 0

        if self.getSize() != 1:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]

        value = self.data.pop()

        self.reBuildingWhenPop()

        return value


if __name__ == "__main__":
    minHeap = MinHeap()

    for j in range(1, 1000):
        # make test data
        testSize = j
        testSet = [i for i in range(1, 1 + testSize)]
        random.shuffle(testSet)

        for i in testSet:
            minHeap.push(i)

        if minHeap.getSize() != testSize:
            print(str(j) + ": Test is fail: MinHeap.getSize()")
            sys.exit(-1)

        for i in range(1, 1 + testSize):
            value = minHeap.pop()
            #print(str(i) + ", " + str(value))

            if i != value:
                print(str(j) +  ": Test is fail: MinHeap")
                sys.exit(-1)

        print(str(j) + ": Test is pass")
