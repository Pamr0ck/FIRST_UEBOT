from collections import deque
queue=deque()
for i in range(10):
    queue.append(i)
print(queue[0])
queue.popleft()
print(queue[0])