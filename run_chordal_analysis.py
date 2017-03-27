import os
from natsort import natsorted, ns
from chordal_analysis import analyze
from chordal_analysis import compare

input_dir = 'kpcorpus'
output_dir = 'output'

ground_truth_dir = 'kpcorpus'
analysis_dir = 'kpanswers'

def run_comparison(ground_truth_dir, analysis_dir):
    files = os.listdir(input_dir)
    files = [x for x in files if x.endswith('.xml')]
    files = natsorted(files, key=lambda y: y.lower())
    scores = []
    for fname in files:
        print '{}'.format(fname)
        fout_xml = '{}.xml'.format(fname[:-4])
        gtruthfile = os.path.join(ground_truth_dir,fname)
        guessfile = os.path.join(analysis_dir,fout_xml)
        score,perc = compare(gtruthfile, guessfile)
        print '\t{}% accuracy'.format(perc)
        scores.append(perc)
    print 'Overall Analysed Files:'
    files_number = len(scores)
    print '\tTotal number of files: {}'.format(files_number)
    print '\tAverage accuracy: {}'.format(sum(scores)/files_number)
    print '\tMinimum accuracy: {}'.format(min(scores))
    print '\tMaximum accuracy: {}'.format(max(scores))

def run_analysis(input_dir, output_dir):
    files = os.listdir(input_dir)
    files = [x for x in files if x.endswith('.xml')]
    files = natsorted(files, key=lambda y: y.lower())
    scores = []
    for fname in files:
        print '{}'.format(fname)
        fout_xml = '{}_analysis.xml'.format(fname[:-4])
        fout_json = '{}_analysis.json'.format(fname[:-4])
        fdir = os.path.join(input_dir,fname)
        if not os.path.exists(os.path.join(output_dir, fout_xml)):
            analyze(fdir, os.path.join(output_dir,fout_xml))

if __name__ == '__main__':
    # Analyze the entire kpcorpus
    run_analysis('kpcorpus', 'kpanalysis_dn')
    # Compare the original annotations of the kpcorpus vs. our analysis
    run_comparison('kpcorpus', 'kpanalysis_dn')
    # Compare the original annotations of the kpcorpus vs. gsp analysis
    run_comparison('kpcorpus', 'kpanalysis_gsp')
