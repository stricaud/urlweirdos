import os
import importlib

class UrlwPlugins:
    def __init__(self, urlwlog, plugins_path=None):
        self.log = urlwlog

        if plugins_path is None:
            self.plugins_path = os.path.dirname(__file__) + os.sep
        else:
            self.plugins_path = plugins_path

        self.plugins_list = self.get_plugins_list(self.plugins_path)
#        print(str(self.plugins_list))
        self.uwplugins = {}
        self.load_plugins(self.plugins_path, self.plugins_list)

    def get_plugins_list(self, plugins_path):
        plugins_list = []
        all_plugins_list = os.listdir(plugins_path)
        for plugin in all_plugins_list:
            filename = plugins_path + plugin + "/__init__.py"
            try:
                f = open(filename, 'r')
                f.close()
                plugins_list.append(plugin)
            except:
                pass

        return plugins_list

    def load_plugins(self, plugins_path, plugins_list):
        for plugin in self.plugins_list:
            modulepath = "urlw.plugins." + plugin
            module = importlib.__import__(modulepath, fromlist=['UrlWeirdosPlugin'])
            self.uwplugins[plugin] = module.UrlWeirdosPlugin(self.log)

    def run(self, plugin_name, url, faup_object):
        self.uwplugins[plugin_name].run(url, faup_object)
