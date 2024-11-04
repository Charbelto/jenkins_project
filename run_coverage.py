import coverage
import unittest

def run_coverage():
    """Run tests with coverage and generate reports."""
    # Start coverage
    cov = coverage.Coverage(config_file='.coveragerc')
    cov.start()

    # Run tests
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    runner = unittest.TextTestRunner()
    runner.run(tests)

    # Stop coverage
    cov.stop()
    cov.save()

    # Generate reports
    print('\nCoverage Summary:')
    cov.report()
    
    print('\nGenerating HTML Report...')
    cov.html_report()
    
    print('\nGenerating XML Report...')
    cov.xml_report()

if __name__ == '__main__':
    run_coverage()