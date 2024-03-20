#!/usr/bin/python3
import apt_pkg
import io
import urllib.request
import html.parser

class SuiteFinder(html.parser.HTMLParser):
    def __init__(self, repository_url):
        super().__init__()
        self._repository_url = repository_url
        self._distro_names = []

    def get(self):
        try:
            with urllib.request.urlopen(f"{self._repository_url}/dists/") as response:
                self.feed(response.read().decode('utf-8'))
                return self._distro_names
        except Exception as e:
            print(f"Failed to retrieve files: {e}")

    def handle_starttag(self, tag, attributes):
         if tag == 'a':
             self._distro_names += (value[:-1] for name, value in attributes if name == "href" and value[0].islower())

class ComponentFinder():
    def __init__(self, repository_url, suite):
        self._repository_url = repository_url
        self._suite = suite

    def get(self):
        with urllib.request.urlopen(f"{self._repository_url}/dists/{self._suite}/Release") as response:
            with apt_pkg.TagFile(response.read().decode('utf-8')) as tf:
                tf.step()
                print(tf.section['Components'])



df = SuiteFinder("http://archive.ubuntu.com/ubuntu")
print(df.get())
cf = ComponentFinder("http://archive.ubuntu.com/ubuntu","bionic")
cf.get()
