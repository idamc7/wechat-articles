from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

class WeatherAgent:
    """
    An agent that generates personalized weather notifications using an LLM.
    """
    def __init__(self, api_key: str):
        self.llm = ChatOpenAI(
            model="deepseek-chat",
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
        self.prompt_template = self._create_prompt_template()
        self.chain = self.prompt_template | self.llm | StrOutputParser()

    def _create_prompt_template(self) -> ChatPromptTemplate:
        """
        Creates the prompt template for the LLM.
        """
        template = """
        你是一位贴心且专业的天气预报员。请根据以下今天的天气数据，为{user_name}生成一条在{city}的中文天气提醒。
        要求：
        1.  以亲切的口吻开始，例如“早上好，亲爱的{user_name}！”。
        2.  总结今天的主要天气，包括：最高/最低温度、白天和晚上的天气状况、风向和风力。
        3.  给出具体的穿衣建议，要考虑到温度范围。
        4.  根据天气（如下雨、强风、高温或低温）给出是否需要带伞或其他实用建议。
        5.  结尾可以加上一句《爱的五种语言》里面的话。
        6.  内容要简洁、友好、信息全面。
        7.  天气是真实的数据，除了以上我要求的信息之外不要附带任何无关信息。

        天气数据:
        {weather_data}
        """
        return ChatPromptTemplate.from_template(template)

    def generate_weather_report(self, user_name: str, city: str, weather_data: dict) -> str:
        """
        Generates a friendly and informative weather report.
        """
        return self.chain.invoke({
            "user_name": user_name,
            "city": city,
            "weather_data": str(weather_data)
        })