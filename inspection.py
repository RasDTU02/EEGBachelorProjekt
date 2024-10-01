import mne
import os

# ----------------------------
# Assumption: UNPROCESSED DATA

#path = 'EDF filer'
#folder = 'L:\\LovbeskyttetMapper\\CONNECT-ME\\cEEG projekt - CONNECT-ME\\EEGer\\Anonymiserede EEGer\\'
#full_path = os.path.join(folder, path)
#raw = mne.io.read_raw_edf(full_path + '\\10GK-EDF+1.edf', preload=True)

#plot
#raw.plot(block = True)
#print(raw.info)

#spectrum = raw.compute_psd()
#spectrum.plot(average=True, picks="data", exclude="bads", amplitude=False)


# ----------------------------


# Assumption: PREPROCESSED DATA
path = 'used_raws'
folder = 'L:\\LovbeskyttetMapper\\CONNECT-ME\\cEEG projekt - CONNECT-ME\\Mappe til Cecilie og Katharina\\nice\\examples\\'
full_path = os.path.join(folder, path)
raw = mne.io.read_raw_fif(full_path + '\\patient10_raw.fif', preload=True)

#plot
raw.plot(block = True)
print(raw.info)

#spectrum = raw.compute_psd()
#spectrum.plot(average=True, picks="data", exclude="bads", amplitude=False)



