from typing import TypedDict
from langgraph.graph import StateGraph,START,END

#define state
class UserState(TypedDict):
    name:str
    age:int
    skills:list[str]
    greetings:str
    age_des:str
    skill_des:str
    result:str

#first node
def greeting_node(state:UserState):
    return {
        "greetings":f"{state['name']},welcome to the system"
    }
#second node
def age_node(state:UserState):
    return{
        "age_des":f"you are {state['age']} years old!!"
    }

#third node
def skills_node(state:UserState):
    skill = state['skills']

    # formatted_skill = ", ".join(skill) if skill else "No skills provided"
    formatted_skill = "- ".join(skill) if skill else "No skills provided"

    # if len(skill) == 1:
    #     formatted_skill = skill[0]
    # elif len(skill) == 2:
    #     formatted_skill = skill[1]

    return{
        "skill_des":f"{formatted_skill} is your skill!!"
    }

# combine message
def result_node(state:UserState):
    result = " ".join((
        state["greetings"],
        state["age_des"],
        state["skill_des"],
    ))

    return {'result':result}

#build graph
builder = StateGraph(UserState)
builder.add_node("greetings",greeting_node)
builder.add_node("age",age_node) 
builder.add_node("skills",skills_node) 
builder.add_node("result",result_node) 

builder.add_edge(START,"greetings")
builder.add_edge("greetings","age")
builder.add_edge("age","skills")
builder.add_edge("skills","result")
builder.add_edge("result", END)

graph = builder.compile()

output = graph.invoke({
    "name": "aks",
    "age": 31,
    "skills": ["Python", "Machine Learning", "LangGraph"],
    "greeting": "",
    "age_description": "",
    "skills_description": "",
    "result": ""
})

print(output["result"])