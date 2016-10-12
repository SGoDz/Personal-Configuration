#include <stdio.h>
#include <string.h>
 
#include <curl/curl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>

static size_t read_callback(void *ptr, size_t size, size_t nmemb, void *stream)
{
  /* in real-world cases, this would probably get this data differently
     as this fread() stuff is exactly what the library already would do
     by default internally */ 
  size_t retcode = fread(ptr, size, nmemb, (FILE *)stream);
 
  //fprintf(stderr, "*** We read %d bytes from file\n", (int)retcode);
  return retcode;
}
 
int ftp_upload( FILE *hd_src, int fsize, const char *fremote, const char *url )
{
  CURL *curl;
  CURLcode res;
 
  struct curl_slist *headerlist=NULL;
  char buf_1 [200];
  
  /* In windows, this will init the winsock stuff */ 
  curl_global_init(CURL_GLOBAL_ALL);
 
  /* get a curl handle */ 
  curl = curl_easy_init();
  if(curl) {
    /* build a list of commands to pass to libcurl */ 
    sprintf( buf_1, "RNFR %s", fremote );
    headerlist = curl_slist_append(headerlist, buf_1);
 
    curl_easy_setopt(curl, CURLOPT_VERBOSE , 1);

    /* we want to use our own read function */ 
    curl_easy_setopt(curl, CURLOPT_READFUNCTION, read_callback);
 
    /* enable uploading */ 
    curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);
 
    /* specify target */ 
    curl_easy_setopt(curl,CURLOPT_URL, url );
 
    /* pass in that last of FTP commands to run after the transfer */ 
    curl_easy_setopt(curl, CURLOPT_POSTQUOTE, headerlist);
 
    /* now specify which file to upload */ 
    curl_easy_setopt(curl, CURLOPT_READDATA, hd_src);
 
    /* Set the size of the file to upload (optional).  If you give a *_LARGE
       option you MUST make sure that the type of the passed-in argument is a
       curl_off_t. If you use CURLOPT_INFILESIZE (without _LARGE) you must
       make sure that to pass in a type 'long' argument. */ 
    curl_easy_setopt(curl, CURLOPT_INFILESIZE_LARGE,
                     (curl_off_t)fsize);
 
    /* Now run off and do what you've been told! */ 
    res = curl_easy_perform(curl);
 
    /* clean up the FTP commands list */ 
    curl_slist_free_all (headerlist);
 
    /* always cleanup */ 
    curl_easy_cleanup(curl);
  }
 
  curl_global_cleanup();
  return res;
}
