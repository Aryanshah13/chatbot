#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def chatbot():
    print("Chatbot: Hello! I'm here to chat with you.what do you need?")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "hello":
            print("Chatbot: Hi there!")
        elif user_input.lower() == "how are you?":
            print("Chatbot: I'm just a program, but I'm functioning well. How about you?")
        elif user_input.lower() == "what's your age?":
            print("Chatbot: I'M ageless")
        elif user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")
            
       

if __name__ == "__main__":
    chatbot()


# In[ ]:




