def Fill_gender_based_on_title(df):
    # Define a mapping for titles to gender
    title_to_gender = {
        'Mr': 'Male',
        'Mrs': 'Female',
        'Miss': 'Female',
        'Ms': 'Female',
        'Dr': 'Male',
    }
    
    # Only update the rows where Gender is 'Not specified'
    df.loc[df['Gender'] == 'Not specified', 'Gender'] = df.loc[df['Gender'] == 'Not specified', 'Title'].map(title_to_gender)

    # Print out the updated counts for validation
    print(df['Gender'].value_counts())

    return df

