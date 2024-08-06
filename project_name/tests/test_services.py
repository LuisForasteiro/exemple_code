import unittest
from src.services.scheduler import run_scheduler
import threading
import time

class TestScheduler(unittest.TestCase):
    def test_run_scheduler(self):
        scheduler_thread = threading.Thread(target=run_scheduler)
        scheduler_thread.start()
        time.sleep(2)
        self.assertTrue(scheduler_thread.is_alive())
        scheduler_thread.join(1)

if __name__ == '__main__':
    unittest.main()
