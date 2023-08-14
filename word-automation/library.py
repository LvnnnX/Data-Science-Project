import numpy as np
import streamlit as st
import pandas as pd
from docx2python import docx2python
from pathlib import Path
import os
import numpy as np
from docx import Document
from docx.shared import Pt
import paragraphs
from docx.enum.text import WD_ALIGN_PARAGRAPH
import io
from docxtpl import DocxTemplate
from datetime import datetime
import colorsys