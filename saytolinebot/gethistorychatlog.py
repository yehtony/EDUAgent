import pymongo
import pymongoconnetion
import json

client = pymongoconnetion.connect_to_mongodb()


class User:
    def __init__(self, userId):
        self.userId = userId

    def get_userId(self):
        return self.userId


user = User(0)


class Agent:
    def __init__(self, AgentId):
        self.agentId = AgentId

    def get_agentId(self):
        return self.agentId


agent = Agent(0)


def get_all_documents(collection, user: User, agent: Agent):
    query = {
        "userId": user.get_userId(),
        "agentId": agent.get_agentId(),
    }
    projection = {
        "userId": 0,
        "agentId": 0,
        "_id": 0,
    }
    documents = collection.find(query, projection)
    return [doc["chatlog"][0] for doc in documents]


def historyChatlog():
    db = client["UserAgentLog"]
    collection = db["historyChatlog"]
    historyChatlog = get_all_documents(collection, user, agent)
    jsonHistoryChatlog = json.dumps(historyChatlog, indent=2, ensure_ascii=False)
    print(jsonHistoryChatlog)
    return historyChatlog


historyChatlog()
