#!/usr/bin/env python

# Import Block
import os           # Get Enviroment Variables
import subprocess   # Run External Code

# Import when not using as a module
import sys          # Get Arguments

# SDHash Adpater Class
class SDHash():
    # 1 or 2 Arguments
    def __init__(self, file1=None, file2=None):
        # Get SDHash binary path from environment variable
        self.__sdhash_bin = "%s/JC-sdhash" % os.environ['SDHASH']
        # Check if first file was provided
        if file1 is None:
            # raise error case not
            raise ValueError("No Input File was provided")
        # store file1 path
        self._file1 = file1
        # compute hash of file1
        self._file1_hashes = self.__compute_hashes(self._file1)
        # check if file2 was provided
        if file2 is not None:
            # store
            self._file2 = file2
            # compute hash
            self._file2_hashes = self.__compute_hashes(self._file2)

    # Compute Hashes
    def __compute_hashes(self, fileN):
        # Build command
        cmd = "%s %s" % (self.__sdhash_bin, fileN)
        # Run Process
        s = subprocess.check_output(cmd.split(" "))
        # Get Output
        return s.strip()

    # Get the original hash string
    def get_hashes(self):
        # check if file1 provided
        if self._file1_hashes is not None:
            # check for file2
            if self._file2_hashes is not None:
                # return the two files
                return self._file1_hashes, self._file2_hashes
            # file2 not provided, return file 1
            return self._file1_hashes
        # no file provided, raise an error
        raise ValueError("Invalid Method Invocation")

    # Compare the two provided files
    def compare(self):
        # check if the two were provided
        if self._file1_hashes is not None and self._file2_hashes is not None:
            # build command with -g (comparison) flag
            cmd = "%s -g %s %s" % (self.__sdhash_bin, self._file1, self._file2)
            # run the command
            s = subprocess.check_output(cmd.split(" "))
            # if no result (no similarity)
            if len(s)==0:
                # build no similarity string
                self._comparison = "No Similarity"
            # case having result
            else:
                # store the resulting string
                self._comparison = s.strip()
            # return result 
            return self._comparison
        # if missing at least one argument, raise an error
        raise ValueError("Invalid Method Invocation")

    # Get hash score
    def get_score(self, comparison=None):
        # if argument provided, use argument
        if comparison is None:
            # if not provided
            if self._comparison is not None:
                # check if we have a previous computation stored
                comparison = self._comparison
                # and use it
            # if no previous result found
            else:
                # raise an error
                raise ValueError("No Previous Comparison")
        # try to interpret result as a sdhash string
        try:
            # if it is, split and get the field
            return float(comparison.split("|")[2])
        # if it is not
        except:
            # return 0
            return 0    # this case happens when no similarity is found

    # same as before, for the JR field
    def get_JR(self, comparison=None):
        if comparison is None:
            if self._comparison is not None:
                comparison = self._comparison
            else:
                raise ValueError("No Previous Comparison")
        try:
            return float(comparison.split("|")[3])
        except:
            return 0

    # same as before, for the JC field
    def get_JC(self, comparison=None):
        if comparison is None:
            if self._comparison is not None:
                comparison = self._comparison
            else:
                raise ValueError("No Previous Comparison")
        try:
            return float(comparison.split("|")[4])
        except:
            return 0

# Testing Case
file1 = sys.argv[1] # First file
file2 = sys.argv[2] # Second file
sdhash = SDHash(file1, file2)                       # instantiate adapter
print("Comparing:\t\t%s and %s" % (file1, file2))   # User Message
print("Comparison String:\t%s" % sdhash.compare())  # Compare Files and Print Resulting String
print("Score:\t\t\t%f" % sdhash.get_score())        # Display Score 
print("JR:\t\t\t%f" % sdhash.get_JR())              # Display JR
print("JC:\t\t\t%f" % sdhash.get_JC())              # Display JC
