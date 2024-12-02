import pytest
import yaml

from data_source import YAPISourceAdapter
from output import OutputGenerator, YamlOutputGenerator


# @pytest.fixture
# def yapi_data():
#     with open("data/yapi.json") as f:
#         data = yaml.safe_load(f)
#     yield data

class TestYamlOutputGenerator:
    def setup_class(self):
        self.yapi = YAPISourceAdapter()


    def test_generate(self, yapi_data):
        origin_data = yapi_data[0].get("list")[0]
        self.api_obj = self.yapi.convert_to_api(origin_data)
        YamlOutputGenerator(self.api_obj).generate("./res/"+"123.yaml")

