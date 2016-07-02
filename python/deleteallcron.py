import os
import sys
from crontab import CronTab
tab = CronTab(user='www-data')
tab.remove_all(comment='music')
tab.write()
print tab.render()
