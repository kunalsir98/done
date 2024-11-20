from pandas_profiling import ProfileReport
import sweetviz as sv

import os
from pandas_profiling import ProfileReport

class EDAReport:
    @staticmethod
    def generate_pandas_report(df, output_file="templates/eda_report.html"):
        # Check if the directory exists, if not, create it
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        try:
            # Generate the profile report
            profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
            # Save the report to the specified file
            profile.to_file(output_file)
            return output_file
        except Exception as e:
            print(f"Error generating the EDA report: {e}")
            return None


    @staticmethod
    def generate_sweetviz_report(df, output_file="templates/sweetviz_report.html"):
        report = sv.analyze(df)
        report.show_html(output_file)
        return output_file
