from model.ind_users import IndUserModel
from model.org_users import OrgUserModel
from model.org_tester import OrgTesterModel

test = OrgTesterModel(12,"123123123", "sadasd", "f", 155, 76, 23, "tests")
test.save_to_db()
