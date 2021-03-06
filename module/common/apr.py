# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class apr(base):
	def install(self):
		self.download(conf.APACHE_OLD + '/apr/' + conf.APR + '.tar.gz')
		self.unzip(conf.APR)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.APR):
			run('./configure --prefix=/usr/local/apr')
			run('make && make install')
		self.download(conf.APACHE_OLD + '/apr/' + conf.APR_UTIL + '.tar.gz')
		self.unzip(conf.APR_UTIL)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.APR_UTIL):
			run('''
				./configure --prefix=/usr/local/apr-util \
				--with-apr=/usr/local/apr
				''')
			run('make && make install')
		run('touch /usr/local/apr/.install.log')

	def check(self):
		return self.test('/usr/local/apr/.install.log')
