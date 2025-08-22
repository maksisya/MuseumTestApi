from pydantic import BaseModel
from datetime import datetime
import requests

# Модель объекта произведения искусства
class MuseumObject(BaseModel):
    objectID: int
    isHighlight: bool
    accessionNumber: str
    accessionYear: str
    isPublicDomain: bool
    primaryImage: str
    primaryImageSmall: str
    additionalImages: list
    constituents: list
    department: str
    objectName: str
    title: str
    culture: str
    period: str
    dynasty: str
    reign: str
    portfolio: str
    artistRole: str
    artistPrefix: str
    artistDisplayName: str
    artistDisplayBio: str
    artistSuffix: str
    artistAlphaSort: str
    artistNationality: str
    artistBeginDate: str
    artistEndDate: str
    artistGender: str
    artistWikidata_URL: str
    artistULAN_URL: str
    objectDate: str
    objectBeginDate: int
    objectEndDate: int
    medium: str
    dimensions: str
    # dimensionsParsed: float
    measurements: list
    creditLine: str
    geographyType: str
    city: str
    state: str
    county: str
    country: str
    region: str
    subregion: str
    locale: str
    locus: str
    excavation: str
    river: str
    classification: str
    rightsAndReproduction: str
    linkResource: str
    metadataDate: datetime
    repository: str
    objectURL: str
    tags: list
    objectWikidata_URL: str
    isTimelineWork: bool
    GalleryNumber: str


# Модель списка произведений искусства
class ObjectsList(BaseModel):
    total: int
    objectIDs: list


if __name__ == '__main__':
    r = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/436803")
    response_dict = r.json()
    MuseumObject(**response_dict)

    r = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?q=sunflowers")
    response_dict = r.json()
    ObjectsList(**response_dict)

