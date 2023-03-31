# Data load for a BMI calculator with CI.

This is a setup approach for a BMI calculator where a **json** file has to be processed with **pandas*, the data will be classified with output prints.

This code can be run locally after executing the `setup_env.sh` file. First, you must change
the file properties with `chmod +x setup_env.sh` . Once the file is executed the project
dependencies will be installed and ready for use.
The sample data is in the data folder and it can be processed running `python3 bmi_calc.py`.
To avoid over complication of the data manipulation, `sqlite3` was used to manipulate the `pandas` **dataframe**. The tests are managed with `pytest` locally and as part of the github actions. See below an example of a failure test:
![alt text](https://user-images.githubusercontent.com/52627521/229082156-beac5fa3-048d-4c4f-82ca-fa24bf62825b.png)

Notice that if the test is not successful, then you are unable to merge the pull request. To activate this feature you must set it up on branches tag. See below screenshot:

![alt text](https://user-images.githubusercontent.com/52627521/228794086-e680b899-f600-4cec-a655-cd7d2ee48e5e.png)
----
