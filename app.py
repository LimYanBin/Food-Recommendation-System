import streamlit as st
from PIL import Image

# Define the menu
menu = {
    1: 'California Roll',
    2: 'Salmon Nigiri',
    3: 'Tonkotsu Ramen',
    4: 'Chicken Teriyaki Bento',
    5: 'Edamame',
    6: 'Gyoza (Dumplings)',
    7: 'Tempura (Shrimp)',
    8: 'Green Tea Ice Cream',
    9: 'Mochi Ice Cream',
    10: 'Matcha Latte'
}

image = {
    1: 'CalRoll.jpg',
    2: 'Salmon.jpg',
    3: 'Ramen.jpg',
    4: 'Chicken.jpg',
    5: 'Edamame.jpg',
    6: 'Gyoza (Dumplings).jpg',
    7: 'Tempura (Shrimp).jpg',
    8: 'Green Tea Ice Cream.jpg',
    9: 'Mochi Ice Cream.jpg',
    10: 'Matcha Latte.jpg'
}

confidence = {
    (1, 9): 0.58,
    (1, 8): 0.56,
    (1, 10): 0.55,
    (2, 8): 0.52,
    (2, 4): 0.51,
    (2, 5): 0.50,
    (3, 9): 0.59,
    (3, 8): 0.52,
    (3, 7): 0.50,
    (4, 9): 0.60,
    (4, 10): 0.51,
    (4, 3): 0.47,
    (5, 9): 0.57,
    (5, 10): 0.57,
    (5, 8): 0.55,
    (6, 10): 0.54,
    (6, 9): 0.53,
    (6, 4): 0.50,
    (7, 3): 0.55,
    (7, 9): 0.55,
    (7, 10): 0.52,
    (8, 9): 0.57,
    (8, 10): 0.53,
    (8, 5): 0.52,
    (9, 3): 0.54,
    (9, 8): 0.54,
    (9, 4): 0.50,
    (10, 5): 0.55,
    (10, 8): 0.54,
    (10, 1): 0.49,
}

st.title('Food Recommendation System')

st.subheader('Menu Items:')
item_number = 1
while item_number <= len(menu):
    col1, col2 = st.columns(2)

    item_name = menu.get(item_number, None)
    
    with col1:
        st.markdown(f"<div style='margin:10px;padding:0px;font-size:20px'>{item_number}.&nbsp;&nbsp;&nbsp;&nbsp;{item_name}</div>", unsafe_allow_html=True)
        image_file = image.get(item_number, None)
        if image_file: 
            image_path = f"Image/{image_file}"
            ig = Image.open(image_path)
            ig = ig.resize((250, 200)) # Resize image
            st.image(ig, caption=item_name, width=250)
    
    item_number += 1
    item_name = menu.get(item_number, None)
    if item_name:
        with col2:
            st.markdown(f"<div style='margin:10px;padding:0px;font-size:20px'>{item_number}.&nbsp;&nbsp;&nbsp;&nbsp;{item_name}</div>", unsafe_allow_html=True)
            image_file = image.get(item_number, None)
            if image_file:
                image_path = f"Image/{image_file}"
                ig = Image.open(image_path)
                ig = ig.resize((250, 200)) # Resize image
                st.image(ig, caption=item_name, width=250)
                item_number += 1

    # If there's no next item for the second column, break the loop to avoid repeating the last item
    if item_name is None:
        break
    

id_number = st.number_input('Enter the ID number:', min_value=1, value=1)

if id_number in menu:
    st.markdown(f"<div style='font-size:24px;margin-bottom:20px'>You had selected: {menu[id_number]}</div>", unsafe_allow_html=True)

    recommendations = [(pair[1], score) for pair, score in confidence.items() if pair[0] == id_number]
    recommendations.sort(key=lambda x: x[1], reverse=True)

    st.markdown(f"<div style='font-size:24px;margin-bottom:10px;padding:20px;background-color:#133853'>Top 3 recommendations for {menu.get(id_number, 'Unknown Item')} are:</div>", unsafe_allow_html=True)

    for idx, (rec_id, score) in enumerate(recommendations[:3], start=1):
        st.markdown(f"<div style='margin:0px;font-size:20px;padding:20px;background-color:#cee9ff;color:#29272d'>{idx}.&nbsp;&nbsp;&nbsp;&nbsp;{menu.get(rec_id, 'Unknown Item')}</div>", unsafe_allow_html=True)

else:
    st.write("Item not found. Please enter a valid ID number.")







