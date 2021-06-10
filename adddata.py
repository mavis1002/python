import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.model import Post

for i in range(10):
	newdata = Post(title = "我的標題{}".format(i+5),
					body = "我的內文{}".format(i+5))

	newdata.save()						Regerences:
								