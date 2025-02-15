import pandas as pd
import streamlit as st
import pickle
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit.components.v1 as components
import codecs

API_KEY = "..."  # Your API key here

st.set_page_config(
    page_title="Movie Recommender App",
    page_icon=":movie_camera:",
    layout="wide",  # Set to "centered" for a more compact design
    initial_sidebar_state="expanded",  # Use "collapsed" to hide the sidebar by default
    #theme="dark"  # Try using the dark theme if available in your Streamlit version
)


hide_menu_style = """
    <style>

    footer {visibility: hidden;}
    </style>
"""

st.markdown(hide_menu_style, unsafe_allow_html=True)

# Option menu with different sections
selected = option_menu(
    menu_title=None,
    options=["Home", "Movies", "Recommendations"],
    icons=["house", "film", "star"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Load HTML content
with open("./template/html/home0.html", "r") as file:
    html_0 = file.read()
with open("./template/html/home1.html", "r") as file:
    html_1 = file.read()
with open("./template/html/home2.html", "r") as file:
    html_2 = file.read()
with open("./template/html/home3.html", "r") as file:
    html_3 = file.read()

# Movie recommendation function
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x1: x1[1]
    )[1:21]

    recommended_movies = []
    for x in movies_list:
        recommended_movies.append(movies.iloc[x[0]].title)
    return recommended_movies

# Load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
bp = 0

#lottie_movie1 = load_lottieurl("https://assets1.lottiefiles.com/datafiles/0BYCsvMJc8EIEvp/data.json")
lottie_movie2 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_CTaizi.json")

# Main page logic, display all sections based on selection
if selected == "Home":
    st.markdown(html_0, unsafe_allow_html=True)
    ct1, ct2 = st.columns((2, 1))
    with ct1:
        st.markdown(html_1, unsafe_allow_html=True)
        # st_lottie(
        #     speed=0.7,
        #     reverse=False,
        #     loop=False,
        #     quality="high",
        #     width=200,
        #     key=None,
        # )
    with ct2:
        st_lottie(
            lottie_movie2,
            speed=0.8,
            reverse=False,
            loop=True,
            quality="high",
            width=250,
            key=None,
        )

elif selected == "Movies":
    # Display the Movies section
    st.markdown(html_2, unsafe_allow_html=True)

elif selected == "Recommendations":
    # Movie recommendation section
    movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open("similarity.pkl", "rb"))

    cm1, cm2, cm3, cm4 = st.columns([1, 31, 5, 1])

    with cm1:
        st.write(" ")
    with cm2:
        selected_movie_name = st.selectbox(
            "Search your favorite movie here...",
            movies["title"].values,
            index=0,
        )
    with cm3:
        st.subheader(" ")
        st.text(" ")
        if st.button("Recommend"):
            m = st.markdown(html_3, unsafe_allow_html=True)
            names = recommend(selected_movie_name)  # Fetch names only
            bp = 1
    with cm4:
        st.write(" ")

    if bp:
        st.header(" ")
        st.markdown(html_3, unsafe_allow_html=True)
        st.header(" ")
        st.markdown("""
        <div style="width: 100%; text-align: center; margin-top: 10px; margin-bottom: 20px;">
            <h2 style="color: #1abc9c; font-family: 'Arial Black', sans-serif;">
                &#x1F3AF; Movie Recommendations for your Search &#x1F3AF;
            </h2>
            <p style="color: #34495e; font-size: 18px; font-family: 'Roboto', sans-serif;">
                Here are some movies you might enjoy based on your selection:
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Create a layout with columns to display cards side by side
        num_columns = 3  # Number of cards per row
        columns = st.columns(num_columns)

        # Display recommended movie names as cards side by side
        movie_count = len(names)
        for i, name in enumerate(names):
            col = columns[i % num_columns]  # Distribute movies across columns
            with col:
                st.markdown(f"""
                <div style="background-color: #ecf0f1; border-radius: 12px; padding: 20px; margin-bottom: 20px; 
                            box-shadow: 0px 2px 8px rgba(0,0,0,0.1); color: #2c3e50; text-align: center; font-size: 16px;">
                    <h4 style="color: #1abc9c; font-family: 'Arial', sans-serif;">{name}</h4>
                </div>
                """, unsafe_allow_html=True)

# import pandas as pd
# import streamlit as st
# import pickle
# import requests
# from streamlit_lottie import st_lottie
# from streamlit_option_menu import option_menu
# from PIL import Image
# import streamlit.components.v1 as components
# import codecs

# API_KEY = "..."  # Your API key here

# st.set_page_config(
#     page_title="Movie Recommender App",
#     page_icon=":movie_camera:",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         "Get Help": "https://www.extremelycoolapp.com/help",
#         "Report a bug": "https://www.extremelycoolapp.com/bug",
#         "About": "# This is a header. This is an *extremely* cool app!",
#     },
# )

# hide_menu_style = """
#     <style>
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     </style>
#     """
# st.markdown(hide_menu_style, unsafe_allow_html=True)

# selected = option_menu(
#     menu_title=None,
#     options=["Home"],
#     icons=["house"],
#     menu_icon="cast",
#     default_index=0,
#     orientation="horizontal",
# )

# # def fetch_poster(movie_id):
# #     response = requests.get(
# #         "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, API_KEY)
# #     )
# #     data = response.json()
# #     print(data)  # Debugging line
# #     return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

# def recommend(movie):
#     movie_index = movies[movies["title"] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(
#         list(enumerate(distances)), reverse=True, key=lambda x1: x1[1]
#     )[1:21]

#     recommended_movies = []
#     for x in movies_list:
#         recommended_movies.append(movies.iloc[x[0]].title)
#     return recommended_movies

# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# bp = 0

# lottie_movie1 = load_lottieurl("https://assets1.lottiefiles.com/datafiles/0BYCsvMJc8EIEvp/data.json")
# lottie_movie2 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_CTaizi.json")
# lottie_proj2 = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_8npirptd.json")
# lottie_proj10 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_o6spyjnc.json")
# lottie_proj11 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_4kx2q32n.json")
# lottie_ty = load_lottieurl("https://assets4.lottiefiles.com/temporary_files/jzVfLn.json")

# with open("./template/html/home0.html", "r") as file:
#     html_0 = file.read()
# with open("./template/html/home1.html", "r") as file:
#     html_1 = file.read()
# with open("./template/html/home2.html", "r") as file:
#     html_2 = file.read()
# with open("./template/html/home3.html", "r") as file:
#     html_3 = file.read()
# # with open("./template/html/home4.html", "r") as file:
# #     html_4 = file.read()
# # with open("./template/html/home5.html", "r") as file:
# #     html_5 = file.read()
# # with open("./template/html/home6.html", "r") as file:
# #     html_6 = file.read()
# # with open("./template/html/home7.html", "r") as file:
# #     html_7 = file.read()
# # with open("./template/html/home8.html", "r") as file:
# #     html_8 = file.read()

# if selected == "Home":
#     st.markdown(html_0, unsafe_allow_html=True)
#     ct1, ct2 = st.columns((2, 1))
#     with ct1:
#         st.markdown(html_1, unsafe_allow_html=True)
#         st_lottie(
#             lottie_movie1,
#             speed=0.7,
#             reverse=False,
#             loop=False,
#             quality="high",
#             width=200,
#             key=None,
#         )
#     with ct2:
#         st_lottie(
#             lottie_movie2,
#             speed=0.8,
#             reverse=False,
#             loop=True,
#             quality="high",
#             width=250,
#             key=None,
#         )

#     movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
#     movies = pd.DataFrame(movies_dict)
#     similarity = pickle.load(open("similarity.pkl", "rb"))

#     cm1, cm2, cm3, cm4 = st.columns([1, 31, 5, 1])

#     with cm1:
#         st.write(" ")
#     with cm2:
#         selected_movie_name = st.selectbox(
#             "Search your favorite movie here...",
#             movies["title"].values,
#             index=0,
#         )
#     with cm3:
#         st.subheader(" ")
#         st.text(" ")
#         if st.button("Recommend"):
#             m = st.markdown(html_2, unsafe_allow_html=True)
#             names = recommend(selected_movie_name)  # Fetch names only
#             bp = 1
#     with cm4:
#         st.write(" ")
        
# if bp:
#     st.header(" ")
#     st.markdown(html_3, unsafe_allow_html=True)
#     st.header(" ")
#     st.markdown("""
#     <div style="width: 100%; text-align: center; margin-top: 30px; margin-bottom: 20px;">
#         <h2 style="color: #1abc9c; font-family: 'Arial Black', sans-serif;">
#             &#x1F3AF; Movie Recommendations for your Search &#x1F3AF;
#         </h2>
#         <p style="color: #34495e; font-size: 18px; font-family: 'Roboto', sans-serif;">
#             Here are some movies you might enjoy based on your selection:
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     # Create a layout with columns to display cards side by side
#     num_columns = 3  # Number of cards per row
#     columns = st.columns(num_columns)

#     # Display recommended movie names as cards side by side
#     movie_count = len(names)
#     for i, name in enumerate(names):
#         col = columns[i % num_columns]  # Distribute movies across columns
#         with col:
#             st.markdown(f"""
#             <div style="background-color: #ecf0f1; border-radius: 12px; padding: 20px; margin-bottom: 20px; 
#                         box-shadow: 0px 2px 8px rgba(0,0,0,0.1); color: #2c3e50; text-align: center; font-size: 16px;">
#                 <h4 style="color: #1abc9c; font-family: 'Arial', sans-serif;">{name}</h4>
#             </div>
#             """, unsafe_allow_html=True)


#     # if bp:
#     #     st.header(" ")
#     #     st.markdown(html_3, unsafe_allow_html=True)
#     #     st.header(" ")
#     #     st.subheader("Movie Recommendations for your Search:")

#     #     # Display the recommended movie names only
#     #     for name in names:
#     #         st.text(name)  # Display only the movie names

# # if selected == "Project":
# #     st.header(" ")
# #     cl1, cl2, cl3 = st.columns(3)
# #     with cl1:
# #         st.text(" ")
# #     with cl2:
# #         st.markdown("<h1 style='text-align: center; color: grey;'>This Project</h1>", unsafe_allow_html=True)
# #     with cl3:
# #         st_lottie(
# #             lottie_proj2,
# #             speed=0.9,
# #             reverse=False,
# #             loop=True,
# #             quality="high",
# #             width=100,
# #             key=None,
# #         )

# #     col1, col2 = st.columns([2, 1])
# #     with col1:
# #         st.markdown(html_4, unsafe_allow_html=True)

# #     with col2:
# #         st_lottie(
# #             lottie_proj10,
# #             speed=1,
# #             reverse=False,
# #             loop=True,
# #             quality="high",
# #             width=500,
# #             key=None,
# #         )

# #     st.subheader(" ")
# #     st.markdown("<h2 style='text-align: left; color: grey;margin-left: 120px;'>Know more about the Project</h2>", unsafe_allow_html=True)

# #     cl21, cl22 = st.columns([1, 2])
# #     with cl21:
# #         st_lottie(
# #             lottie_proj11,
# #             speed=0.6,
# #             reverse=False,
# #             loop=True,
# #             quality="high",
# #             width=400,
# #             key=None,
# #         )
# #     with cl22:
# #         st.subheader(" ")
# #         st.subheader(" ")
# #         st.markdown(html_5, unsafe_allow_html=True)
# #         st.markdown(html_6, unsafe_allow_html=True)

# # if selected == "About Us":
# #     st.subheader(" ")
# #     st.subheader(" ")

# #     with open("./template/style.css") as f:
# #         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# #     img1 = Image.open("template/images/img11.png")
# #     col1, col2, col3 = st.columns(3)
# #     with col2:
# #         st.image(img1, caption=" ")
# #         st.markdown(html_7, unsafe_allow_html=True)
# #         st.text(" ")
# #         st.text(" ")
# #         st.markdown(html_8, unsafe_allow_html=True)

# #     def about_tab(about_html, width=1200, height=1000):
# #         about_file = codecs.open(about_html, "r")
# #         page = about_file.read()
# #         components.html(page, width=width, height=height, scrolling=True)
