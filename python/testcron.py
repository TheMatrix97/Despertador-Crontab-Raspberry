import os
import sys
from crontab import CronTab
min = sys.argv[1]
hour = sys.argv[2]
#print hour
#min = 2
#hour = 2
tab = CronTab(user='www-data')
cmd = '/usr/bin/python /var/www/test/pgms/python/bdtest.py'
cron_job = tab.new(cmd, comment='music')
cron_job.minute.on(min)
cron_job.hour.on(hour)

#tab.remove_all(comment='test')
tab.write()
print tab.render()
