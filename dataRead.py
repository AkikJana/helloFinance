import os

from QuantConnect import Globals, SubscriptionTransportMedium
from QuantConnect.Data import SubscriptionDataSource
from QuantConnect.Python import PythonData


class customDataRead(PythonData):
    def GetSource(self, config, date, is_live):
        # Old:
        # source = "https://www.dropbox.com/s/8v6z949n25hyk9o/custom_weather_data.csv?dl=1"
        # return SubscriptionDataSource(source, SubscriptionTransportMedium.RemoteFile)

        # New:
        # Replace custom_weather_data.csv with the path to your data file in the data directory
        source = os.path.join(Globals.DataFolder, "BTCUSDT_MinuteBars.csv")
        return SubscriptionDataSource(source, SubscriptionTransportMedium.LocalFile)