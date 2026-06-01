#!/usr/bin/env python
from crewai.flow import Flow, persist, start

from do_recife_chat_flow.agents import DoRecifeAgent
from do_recife_chat_flow.types import Conversation, Message


@persist()
class DoRecifeChatFlow(Flow[Conversation]):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.agent = DoRecifeAgent()

    @start()
    def chat(self):
        self.state.messages.append(self.state.user_message)
        answer = self.agent.answer(self.state.messages)
        self.state.messages.append(Message(role="assistant", content=answer))

        return self.state.model_dump()


def kickoff():
    DoRecifeChatFlow().kickoff(
        inputs={
            "user_message": {
                "role": "user",
                "content": "Quais novidades a cidade do Recife implantou com relação à saúde da mulher?",
            }
        }
    )


def plot():
    DoRecifeChatFlow().plot()


def run_with_trigger():
    """Run the chat flow (trigger payload is not used here)."""
    kickoff()


if __name__ == "__main__":
    kickoff()
