# double Ended Queue
from collections import deque
from icecream import ic

queue = deque(["First", "Second", "Third"])

ic(queue)

ic(queue.append("Fourth"), queue)

ic(queue.popleft(), queue)
