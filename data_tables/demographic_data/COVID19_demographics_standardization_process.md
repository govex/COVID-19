# Standardization Process

In order to create a dataset where the demographic categories are comparable between states, we need to follow an standardization process that in some cases involve making assumptions. This process is detailed below.


### For each State:
---
1. Unify naming conventions
    - Unify naming of unknowns by renaming categories that represent unknowns. (i.e. `not_reported`, `not_available`, `missing`, etc.)
    - Create a consistent naming convention for demographic categories
        - Separate mixed categories with a hyphen (-)
        - Set all data to lower case
        - Unify differently named categories that represent the same group. (i.e. change `hispanic_or_latino` to `hispanic_latino`)
        - Generalize specific racial groups to broader categories (i.e. change `filipino` to `asian`)
        - Decisions on how to rename and recategorize race and ethnicity groups based on guidance from [Office of Management and Budget Standards for Maintaining, Collecting, and Presenting Federal Data on Race and Ethnicity](https://www.federalregister.gov/documents/2016/09/30/2016-23672/standards-for-maintaining-collecting-and-presenting-federal-data-on-race-and-ethnicity)
---
2. Filter data to only contain `Estimate_type` equal to `total_cumulative` or `rate_percent`, which are the most informative estimates when it comes to compare incidence and disparities across states. 
---
3. Aggregate mixed categories when possible (for example, age & sex/gender to obtain age on one side, and sex/gender on the other)
    - Check each component of the mixed category. If the state does not already have that component as a separate data point and if the mixed catgegory can effectively split, then the new category can be aggregated. Check this for each date.
    - This is done for the following mixed categories:
        - `race_ethnicity`
        - `race_age`
        - `ethnicity_age`
        - `gender_sex_race`
        - `age_gender_sex`
---
4.  Drop mixed categories where a state already has each component, with the exception or `race_ethnicity`. For example, if a state provides `age` and `gender_sex`, then `age_gender_sex` would be dropped.
---
5. Convert the existing age ranges to standardized ranges: 
    - Assume uniform distribution across existing age ranges and assume the max age is `100`
    - Divide the value in the existing age range by the number of years in it, and assign each individual age that dividend. Add an exception for vaccines, ages below 12 are assigned a value of `0`. 
    - Group the ages together by the desiered age ranges using the sum of the group to get the standardized age. 
---
6. Calculate rate_percent where missing or if we determine it needs to be recalculated
    - If a state only provides `total_cumulative` for a certain demographic category, then `rate_percent` is derived for each new row using the `total_cumulative` values. 
    - If we determine that a state's provided `rate_percent` data is incorrect, and `total_cumulative` values are available, then replace them with calculated values.
