import al_papi
from distutils.core import setup
setup(
    name="al_papi",
    version="0.0.1",
    description="AuthorityLabs",
    author="Chavez",
    author_email="support@authoritylabs.com",
    url="http://www.api.authoritylabs.com",
    packages=["al_papi"],
    package_data={},
    install_requires=["simplejson"],
    tests_require=["nose", "pinocchio=0.3"],
    zip_safe=False
)
