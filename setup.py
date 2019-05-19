from setuptools import setup, find_packages


def readme():
    """Include README.rst content in PyPi build information"""
    with open('README.md') as file:
        return file.read()

setup(
    name='UnleashClient',
    version='2.3.0',
    author='Ivan Lee',
    author_email='ivanklee86@gmail.com',
    description='Python client for the Unleash feature toggle system!',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/Unleash/unleash-client-python',
    packages=find_packages(),
    install_requires=["requests==2.21.0",
                      "fcache==0.4.7",
                      "mmh3==2.5.1",
                      "APScheduler==3.6.0",
                      "ipaddress==1.0.22",
                      "chainmap==1.0.3"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ]
)
