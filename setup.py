from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'requests_html',
    'beautifulsoup4',
    'youtube_dl',
    'pathlib',
    'pandas'
]

setup(
    name='SpotifyTopSongs',
    version='1.0',
    description='An application that gets your top songs from Spotify',
    author='Mainak Debnath',
    author_email='debnath.mainak07@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)