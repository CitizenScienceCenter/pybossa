from setuptools import setup, find_packages

with open("pybossa/version.txt") as f:
    version = f.readline()
__version__ = version.rstrip()

## Dependencies installed on CSZ legacy pybossa system not listed in setup.py
# cachelib==0.1.1
# cachetools==4.2.2
# dnspython==2.1.0
# Flask-OAuthlib==0.9.6
# frozendict=1.2
# google-api-core==1.26.3
# google-auth==1.30.0
# google-auth-httplib2==0.1.0
# googleapis-common-protos==1.53.0
# greenlet==1.0.0
# os-diskconfig-python-novaclient-ext==0.1.3
# os-networksv2-python-novaclient-ext==0.26
# os-virtual-interfacesv2-python-novaclient-ext==0.20
# packaging==20.9
# protobuf==3.15.8
# rax-default-network-flags-python-novaclient-ext==0.4.0
# rax-scheduled-images-python-novaclient-ext==0.3.1
# Redis-Sentinel-Url==1.0.1

## Dependencies listed not installed on legacy system
# sqlalchemy-json==0.4.0
requirements = [
    "alembic==1.5.8",
    "arrow==1.1.0",
    "asn1crypto==1.4.0",
    "Babel==2.9.0",
    "beautifulsoup4==4.9.3",
    "blinker==1.4",
    "certifi==2023.7.22",
    "cffi>=1.11.5",
    "chardet==4.0.0",
    "Click==8.0.3",
    "colorama==0.4.4",
    "cov-core==1.15.0",
    "coverage==5.5",
    "croniter==1.0.12",
    "cryptography==3.4.7",
    "cssselect==1.1.0",
    "debtcollector==2.2.0",
    "decorator==5.0.7",
    "email-validator==1.1.2",
    "entrypoints==0.3",
    "factory-boy==3.2.0",
    "Faker==8.1.1",
    "feedparser==6.0.2",
    "Flask==1.1.2",
    "Flask-Assets==2.0",
    "Flask-Babel>=0.9",
    "Flask-Cors>=3.0.2",
    "Flask-DebugToolbar==0.11.0",
    "Flask-HTTPAuth>=3.2.4",
    "flask-json-multidict>=1.0.0",
    "Flask-Login>=0.4.1",
    "Flask-Mail>=0.9.1",
    "Flask-Misaka>=1.0.0",
    "Flask-Plugins>=1.6.1",
    "flask-profiler==1.8.1",
    "Flask-SimpleLDAP>=1.1.2",
    "Flask-SQLAlchemy==2.5.1",
    "Flask-WTF==0.14.3",
    "flatten-json==0.1.6",
    "google-api-python-client==2.3.0",
    "html2text==2020.1.16",
    "httplib2==0.19.1",
    "humanize==3.4.1",
    "idna==2.10",
    "iiif-prezi>=0.2.9",
    "infinity==1.5",
    "intervals==0.9.1",
    "iso8601==0.1.14",
    "itsdangerous==1.1.0",
    "jeepney==0.4",
    "Jinja2==2.11.3",
    "jsmin==2.2.2",
    "keyring==21.0.0",
    "keystoneauth1==4.3.1",
    "libsass==0.20.1",
    "lxml==4.6.3",
    "Mako==1.1.4",
    "Markdown==3.3.4",
    "MarkupSafe==1.1.1",
    "misaka==2.1.1",
    "mock==4.0.3",
    "msgpack==1.0.2",
    "ndg-httpsclient==0.5.1",
    "netaddr==0.8.0",
    "netifaces==0.10.9",
    "nose==1.3.7",
    "nose-cov==1.6",
    "numpy==1.20.2",
    "oauth2client==4.1.3",
    "oauthlib==2.1.0",
    "os-service-types==1.7.0",
    "oslo.config==8.6.0",
    "oslo.i18n==5.0.1",
    "oslo.serialization==4.1.0",
    "oslo.utils==4.8.0",
    "otpauth==1.0.1",
    "pandas==1.2.4",
    "pbr>=1.10.0",
    "Pillow>=6.2.0",
    "prettytable==2.1.0",
    "psycopg2-binary>=2.8.6",
    "pyasn1==0.4.8",
    "pyasn1-modules==0.2.8",
    "pybossa-onesignal==1.1",
    "pycountry",
    "pycparser==2.20",
    "pycryptodome==3.10.1",
    "PyJWT==2.1.0",
    "PyLD==2.0.3",
    "pyldap==3.0.0.post1",
    "pyOpenSSL==18.0.0",
    "pyparsing==2.4.7",
    "python-dateutil==2.8.1",
    "python-editor==1.0.4",
    "python-keystoneclient==4.2.0",
    "python-ldap==3.3.1",
    "python-novaclient>=2.27.0",
    "pytz==2021.1",
    "PyYAML==5.4.1",
    "rackspace-auth-openstack==1.3",
    "rackspace-novaclient>=2.1",
    "raven==6.10.0",
    "readability-lxml==0.8.1",
    "redis==3.5.3",
    "rednose==1.3.0",
    "requests==2.25.1",
    "requests-oauthlib==1.1.0",
    "rfc3986==1.4.0",
    "rq==0.13.0",
    "rq-dashboard==0.3.12",
    "rq-scheduler==0.9",
    "rsa>=4.0",
    "SecretStorage==3.1.1",
    "simplejson==3.17.0",
    "six==1.15.0",
    "soupsieve==2.2.1",
    "speaklater==1.3",
    "SQLAlchemy==1.4.11",
    "sqlalchemy-json==0.4.0",
    "stevedore>=1.30.0",
    "termstyle==0.1.11",
    "text-unidecode==1.3",
    "twitter==1.18.0",
    "Unidecode==1.2.0",
    "uritemplate==3.0.1",
    "urllib3==1.26.4",
    "validators==0.18.2",
    "webassets==2.0",
    "Werkzeug==1.0.1",
    "wrapt==1.12.1",
    "WTForms==2.3.3",
    "WTForms-Components==0.10.5",
    "yacryptopan==1.0.1",
]

setup(
    name="pybossa",
    version=__version__,
    packages=find_packages(),
    install_requires=requirements,
    # only needed when installing directly from setup.py (PyPi, eggs?) and pointing to e.g. a git repo.
    # Keep in mind that dependency_links are not used when installing with requirements.txt
    # and need to be added redundant to requirements.txt in this case!
    # Example:
    # dependency_links = [
    #     'git+git@github.com:Scifabric/pybossa.git@b8ab2ef199e82ca417d470bbed916c7b8dbda4d4#egg=pybossa'
    # ]
    # metadata for upload to PyPI
    author="Scifabric LTD",
    author_email="info@scifabric.com",
    description="Open Source CrowdSourcing framework",
    long_description="""PYBOSSA is the ultimate crowdsourcing framework to analyze or enrich data that can't be processed by machines alone.""",
    license="AGPLv3",
    url="http://pybossa.com",
    download_url="https://github.com/Scifabric/pybossa",
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points="""
    """,
)
