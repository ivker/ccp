from encode.interpreter.IOneHotInterpreter import IOneHotInterpreter


class OneHotInterpreter(IOneHotInterpreter):
    """
    解释数据维度的识别信息
    """

    def __init__(self, encode_dimensions: list):
        super().__init__()
        self.onehot_dimension = "onehotid"  # 用于存储编码唯一码的字段
        self.encode_dimensions = encode_dimensions

    def onehot(self, record: dict) -> str:
        """
        返回onehot值
        :param record:
        :return:
        """
        return record.get(self.onehot_dimension)

    def encodes(self, record: dict) -> dict:
        """
        输出数据的编码维度及其值
        :param record:
        :return:
        """
        r = {}
        for encode in self.encode_dimensions:
            r[encode] = record[encode]
        return r