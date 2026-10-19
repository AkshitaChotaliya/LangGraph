from typing import TypedDict
from langgraph.graph import StateGraph,START,END


#state
class ComplimentSate(TypedDict):
    name:str
    quality:str
    interest:str
    compliment:str


#create node
def generate_compliment(state:ComplimentSate):
    name = state["name"]
    quality = state["quality"]
    interest = state["interest"]

    compliment = (
        f"{name},your :: {quality}"
        f"you interest :: {interest}"
    )

    return {"compliment": compliment}


#create graph
builder = StateGraph(ComplimentSate)

#add the node
builder.add_node("generate_compliment", generate_compliment)

#connect the steps
builder.add_edge(START,"generate_compliment")
builder.add_edge("generate_compliment",END)

compilement_agent = builder.compile()

name = input("Enter your name: ")
quality = input("Enter your best quality: ")
interest = input("Enter your interest: ")

result = compilement_agent.invoke({
    "name": name,
    "quality": quality,
    "interest": interest,
    "compliment": ""
})

print("\nYour personalized compliment:")


# result = compilement_agent.invoke({
#     "name" : "AKS",
#     "quality" : "hardworking",
#     "interest" : "python programming",
#     "compliment" : ""
# })

print(result["compliment"])
# name = input("Enter your name: ")
# quality = input("Enter your best quality: ")
# interest = input("Enter your interest: ")

 
