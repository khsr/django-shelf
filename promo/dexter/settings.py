# Scrapy settings for dexter project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'dexter'
BOT_VERSION = '1.0'

DOWNLOAD_DELAY = 5 

RANDOMIZE_DOWNLOAD_DELAY = True

#ROBOTSTXT_OBEY = True

SPIDER_MODULES = ['dexter.spiders']
NEWSPIDER_MODULE = 'dexter.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'dexter.pipelines.DuplicatesPipeline',
]

def setup_django_env(path):
    import imp
    from django.core.management import setup_environ
    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)
    print "Setting django environment: ", project
    setup_environ(project)


setup_django_env('../../miami_metro/')

