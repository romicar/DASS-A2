import sys
import termios
import tty
import signal
from time import sleep

class Get:
    """Class to get input."""

    def _call_(self):
        """Defining _call_."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = str(sys.stdin.read(1))
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def alarmHandler(self,signum, frame):
        """Handling timeouts."""
        raise TimeoutError

    def get_input(self, timeout=0.1):
        """Taking input from user."""
        signal.signal(signal.SIGALRM, self.alarmHandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = self._call_()
            signal.alarm(0)
            if(text == 'w'):
                text = "w"
            # elif text == 'd':
            #     text = "d"
            
            # # else:
            # #     text = None
            sleep(timeout)
            return text
        except TimeoutError:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return None