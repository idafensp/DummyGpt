import streamlit as st

# create a class called ChatMessage
# it contains a role and a content
# content is a list with a list of dictionaries
# each dictionary has a type and a content, which can be an object
class ChatMessage:
    def __init__(self, role):
        self.role = role
        self.content = []

    def __repr__(self):
        return f"ChatMessage(role={self.role}, content={self.content})"
    
    def __str__(self):
        return f"ChatMessage(role={self.role}, content={self.content})"
    
    def __eq__(self, other):
        return self.role == other.role and self.content == other.content
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.role, self.content))
    
    # define and add a method to the class called add_content
    # it takes a type and a content
    # it adds the type and content to the content dictionary
    def add_content(self, type, content):
        self.content.append({'type':type, 'content':content})

    # define a display method that creates a st.chat_message object with the role and the content
    def display(self):
        with st.chat_message(self.role):
            for content in self.content:
                if content["type"] == "markdown":
                    st.markdown(content["content"])
                elif content["type"] == "bar_chart":
                    st.bar_chart(content["content"])
                elif content["type"] == "map":
                    st.map(content["content"])
                elif content["type"] == "image":
                    st.image(content["content"])
                else:
                    st.write(content["content"])


