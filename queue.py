# python 的队列
# 生产者/消费者练习
import time
import random
from queue import Queue
from threading import Thread


# 生产者

class Producer(Thread):

  # python 版本的构造方法 好丑陋...
  # 相当于 js 的 constructor(queue) {
  #  this.queue = queue
  # }
  def __init__(self, queue):
    super().__init__()
    self.queue = queue

  def run(self):
    while True:
      a = random.randint(0, 10)
      b = random.randint(0, 10)
      self.queue.put((a, b))

      # 等待两秒
      time.sleep(2)
