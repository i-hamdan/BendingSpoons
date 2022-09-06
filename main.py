import streamlit as st
import pandas as pd

quarter = pd.read_pickle('quarter_complete.pkl')
month = pd.read_pickle('month_complete.pkl')

st.title('30 Day Fitness - Bending Spoons')
st.subheader('An interactive Play Store ratings analyzer - Hamdan')
st.write('')
st.write('')
st.write('')

unit = st.select_slider('Timeframe', options=('quarter', 'month'))
if unit == 'quarter':
    df = quarter
    pat = 'img_quarter/'
    idl = 3
    idr = 10
else:
    df = month
    pat = 'img_month/'
    idl = 11
    idr = 25

st.line_chart(df, x= unit, y='overall')



col1, col2 = st.columns(2)

dic = {}
for i in range(len(df)):
    dic[df.iloc[i,0]] = unit + str(i) + '.jpg'

with col1:

    left1 = st.selectbox('left', df[unit], index=idl)


    st.metric('Current Rating', df.loc[df[unit] == left1].overall.item())

    img_path = pat + dic[left1]
    st.image(img_path)

    bis = df.loc[df[unit] == left1].bi.item()
    dfs = pd.DataFrame(bis)
    dfs.columns = ['Top Bigrams']
    st.table(dfs)

    tris = df.loc[df[unit] == left1].tri.item()
    dfs = pd.DataFrame(tris)
    dfs.columns = ['Top Trigrams']
    st.table(dfs)



with col2:
    left2 = st.selectbox('right', df[unit], index=idr)

    st.metric('Current Rating', df.loc[df[unit] == left2].overall.item())

    img_path = pat + dic[left2]
    st.image(img_path)

    bis = df.loc[df[unit] == left2].bi.item()
    dfs = pd.DataFrame(bis)
    dfs.columns = ['Top Bigrams']
    st.table(dfs)

    tris = df.loc[df[unit] == left2].tri.item()
    dfs = pd.DataFrame(tris)
    dfs.columns = ['Top Trigrams']
    st.table(dfs)



st.write('')
st.write('')
st.write('')
st.write('')
st.write()
st.write()
st.line_chart(df, x=unit, y='rating')
col3, col4 = st.columns(2)

with col3:
    st.metric('Most Helpful Rating', df.loc[df[unit] == left1].rating.item())

    help_rev = (df.loc[df[unit] == left1]['review']).item()
    st.write(help_rev)

with col4:
    st.metric('Most Helpful Rating', df.loc[df[unit] == left2].rating.item())

    help_rev = (df.loc[df[unit] == left2]['review']).item()
    st.write(help_rev)