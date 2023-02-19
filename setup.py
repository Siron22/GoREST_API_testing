from distutils.core import setup

setup(name='GoREST_API_testing',
      version='1.0',
      description='Little framework with automated tests for GoREST service',
      packages=['to_delete'],
      install_requires=['pytest',
                        'selenium',
                        'webdriver-manager',
                        'allure-pytest',
                        'requests'
                        ]
      )
