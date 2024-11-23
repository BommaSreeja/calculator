import streamlit as st
st.title("FLAMES GAME")
n=list(st.text_input("enter first name"))
m=list(st.text_input("enter second name"))
for char in n:
    if char in m:
        m.remove(char)
        n.remove(char)
res=len(n+m)
s="flames"
while(len(s)!=1):
    i=res%len(s)-1
    if(i==-1):
        s=s[:len(s)-1]
    else:
        s=s[i+1:]+s[:i]
dict={'f':'friendship','l':'love','a':'affection','m':'marriage','e':'engaged','s':'siblings'}
if (st.button("SUBMIT")):
    st.success(dict[s])