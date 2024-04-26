function rrinterval = leerrinterval(archivotxt)
    fileID = fopen(archivotxt);
    A = textscan(fileID,'%s%s%f%s%s');
    fclose(fileID);
    rrinterval = A{1,3};
end