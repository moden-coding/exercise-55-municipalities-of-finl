#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import pandas as pd

from src.municipalities_of_finland import municipalities_of_finland, main


class TestMunicipalitiesOfFinland(unittest.TestCase):

    def test_shape(self):
        df = municipalities_of_finland()
        self.assertEqual(
            df.shape,
            (311, 6),
            msg="municipalities_of_finland() should return a DataFrame with "
            "shape (311, 6): 311 municipalities and 6 data columns. Got "
            "%r." % (df.shape,),
        )

    def test_called(self):
        with patch(
            "src.municipalities_of_finland.municipalities_of_finland",
            wraps=municipalities_of_finland,
        ) as pm:
            main()
            pm.assert_called()
        with patch(
            "src.municipalities_of_finland.pd.read_csv", wraps=pd.read_csv
        ) as prc:
            municipalities_of_finland()
            prc.assert_called()

    def test_content(self):
        df = municipalities_of_finland()
        self.assertEqual(
            df.index[0],
            "Akaa",
            msg="The first row's index should be 'Akaa'. Got %r." % (
                df.index[0],
            ),
        )
        self.assertEqual(
            df.index[-1],
            "Äänekoski",
            msg="The last row's index should be 'Äänekoski'. Got "
            "%r." % (df.index[-1],),
        )
        self.assertEqual(
            df.iloc[0, 0],
            16769,
            msg="The value in the top-left corner of the DataFrame should "
            "be 16769. Got %r." % (df.iloc[0, 0],),
        )
        self.assertEqual(
            df.iloc[-1, -1],
            30.5,
            msg="The value in the bottom-right corner of the DataFrame "
            "should be 30.5. Got %r." % (df.iloc[-1, -1],),
        )


if __name__ == "__main__":
    unittest.main()
