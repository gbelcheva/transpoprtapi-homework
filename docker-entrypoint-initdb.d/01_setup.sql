-- noinspection SqlNoDataSourceInspectionForFile

CREATE TABLE stops (
    ATCOCode TEXT PRIMARY KEY,
    NaptanCode TEXT,
    PlateCode TEXT,
    CleardownCode TEXT,
    CommonName TEXT,
    CommonNameLang TEXT,
    ShortCommonName TEXT,
    ShortCommonNameLang TEXT,
    Landmark TEXT,
    LandmarkLang TEXT,
    Street TEXT,
    StreetLang TEXT,
    Crossing TEXT,
    CrossingLang TEXT,
    Indicator TEXT,
    IndicatorLang TEXT,
    Bearing TEXT,
    NptgLocalityCode TEXT,
    LocalityName TEXT,
    ParentLocalityName TEXT,
    GrandParentLocalityName TEXT,
    Town TEXT,
    TownLang TEXT,
    Suburb TEXT,
    SuburbLang TEXT,
    LocalityCentre TEXT,
    GridType TEXT,
    Easting TEXT,
    Northing TEXT,
    Longitude FLOAT8,
    Latitude FLOAT8,
    StopType TEXT,
    BusStopType TEXT,
    TimingStatus TEXT,
    DefaultWaitTime TEXT,
    Notes TEXT,
    NotesLang TEXT,
    AdministrativeAreaCode TEXT,
    CreationDateTime TEXT,
    ModificationDateTime TEXT,
    RevisionNumber TEXT,
    Modification TEXT,
    Status TEXT
);
