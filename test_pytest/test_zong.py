import pytest
import yaml

from loginn.login_pc import Login


class TestLogin:
    @pytest.mark.parametrize("login_id,password",yaml.load(open("/Users/lyy/pyth/WeLMS_PC/filess/loginj.yaml","r")))
    def test_loginn(self,login_id,password):
        logg=Login()
        logg.login(login_id,password)







