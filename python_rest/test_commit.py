CREATE TABLE Norb_table(
    Id INT PRIMARY KEY NOT NULL,
    Year INT  NOT NULL,
    Month INT NOT NULL,
    Res INT,
    solids BOOLEAN,
    NTU BOOLEAN,
    org_ml BOOLEAN,
    MPN_100ml BOOLEAN,
    MPN_100ml__1 BOOLEAN,
    LosR FLOAT,
    Silica FLOAT,
    Ca  FLOAT,
    Mg FLOAT,
    Ca_Mg FLOAT,
    NO3 FLOAT,
    NO3_USGS FLOAT,
    Cl2 FLOAT,
    Na FLOAT,
    SO4 FLOAT,
    K FLOAT,
    pH FLOAT,
    Alk FLOAT,
    Hard FLOAT,
    Nhard FLOAT,
    C_USGSTemp FLOAT,
    F_USGS FLOAT,
    Temp FLOAT,
    MD_Precip_inch_mon FLOAT,
    MD_Temp_F FLOAT
);

\COPY test_table FROM 'C:\Users\icprbadmin\Documents\Python_Scripts\python_rest\Reservoir_intake.csv' DELIMITER ';' CSV HEADER;
C:\Users\icprbadmin\Documents\Python_Scripts\python_rest

COPY Norb_table FROM 'Reservoir_intake_tweaked.csv' DELIMITER ',' CSV HEADER;

\COPY Norb_table FROM '/Users/lukevawter/Desktop/Python_ICPRB/Aqueduct_API/python_rest/Reservoir_intake_tweaked.csv' DELIMITER ',' CSV HEADER;

/Users/lukevawter/Desktop/Python_ICPRB/Aqueduct_API/python_rest