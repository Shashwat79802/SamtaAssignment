from django.http.response import JsonResponse
from django.http.response import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class StudentListView(APIView):

    def get(self, request):
        data = Student.objects.all()
        if data:
            serializer = StudentSerializer(data, many=True)
        else:
            return Response(data={"message": "No Student exists!!"}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Student created successfully"}, status=status.HTTP_201_CREATED)
        return Response(data={"message": "Failed to create student!!"}, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):

    def get_by_id(self, pk):
        try:
            return Student.objects.get(id=pk)
        except Student.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        data = self.get_by_id(pk)
        serializer = StudentSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        student_to_update = self.get_by_id(pk)
        serializer = StudentSerializer(instance=student_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Student Updated Successfully"}, status=status.HTTP_200_OK)
        return Response(data={"message": "Failed to update student!!"}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        student_to_delete = self.get_by_id(pk)
        student_to_delete.delete()
        return Response(data={"message": "Student Deleted Successfully"}, status=status.HTTP_200_OK)