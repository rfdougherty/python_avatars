import python_avataaars as pa

pa.Avatar(
    style=pa.AvatarStyle.CIRCLE,
    background_color='#FF00FF',
    # Choose graphic shirt
    clothing=pa.ClothingType.GRAPHIC_SHIRT,
    clothing_color=pa.ClothingColor.GRAY_02,
    # Important to choose this as shirt_graphic, otherwise shirt_text will be ignored
    shirt_graphic=pa.ClothingGraphic.CUSTOM_TEXT,
    shirt_text='Chess'
).render("avatar_text.svg")
