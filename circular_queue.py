class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    # enQueue(): 리어 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # deQueue(): 프론트 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True


class CircularQueue:  
  def __init__(self, k: int):
    self._data = [None] * k
    self._rearIdx = -1
    self._frntIdx = 0
    self._size = 0

  def enQueue(self, value: int):
    self._fullCheck()
  
    self._rearIdx += 1
    self._rearIdx = self._rearIdx % len(self._data)
    self._data[self._rearIdx] = value
    self._size += 1


  def deQueue(self):
    self._emptyCheck()

    self._frntIdx +=1
    self._frntIdx = self._frntIdx % len(self._data)
    self._size -= 1
  

  def Rear(self) -> int:
    self._emptyCheck()
    return self._data[self._rearIdx]
    

  def Front(self) -> int:
    self._emptyCheck()
    return self._data[self._frntIdx]
  
  def _emptyCheck(self):
    if self._size == 0:
      raise RuntimeError('Queue is Empty')


  def _fullCheck(self):
    cap = len(self._data)
    if self._size == cap:
       raise RuntimeError('Queue is full')

if __name__ == '__main__':
    queue = MyCircularQueue(6)
    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(3)
    queue.enQueue(4)
    queue.enQueue(5)
    queue.enQueue(6)
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.p1)
    