#include <iostream>
#include "Matrix.h"

Matrix::Matrix(const size_t& _rows, const size_t& _cols, const int& default_value):
	rows(_rows),
	cols(_cols),
	data(std::vector<Row>(rows, Row(cols, default_value)))
{
}

Matrix::~Matrix()
{
}

const size_t Matrix::getRows() const
{
	return rows;
}

const size_t Matrix::getColumns() const
{
	return cols;
}

const Matrix::Row& Matrix::operator[](const size_t& i) const
{
	if (i < rows && !data.empty())
		return data[i];
	else
		throw std::out_of_range("wrong row index");
}

Matrix::Row& Matrix::operator[](const size_t& i)
{
	if (i < rows && !data.empty())
		return data[i];
	else
		throw std::out_of_range("wrong row index");
}

bool Matrix::operator==(const Matrix& other) const
{
	if (this == &other)
		return true;
	if (cols != other.cols || rows != other.rows)
		return false;
	for (size_t i = 0; i < rows; ++i)
		for (size_t j = 0; j < cols; ++j)
			if (data[i][j] != other[i][j])
				return false;
	return true;
}

bool Matrix::operator!=(const Matrix& other) const
{
	return !(*this == other);
}

Matrix& Matrix::operator=(const Matrix& m)
{
	if (this == &m)
		return *this;

	if (!((this)->rows == m.getRows() && (this)->cols == m.getColumns()))
	{
		if(data.size() != 0)
			data.clear();
		rows = m.getRows();
		cols = m.getColumns();
		for (size_t i = 0; i < rows; ++i)
			data.push_back(Row(cols));
	}
	else
	{
		rows = m.getRows();
		cols = m.getColumns();
	}
	for (size_t i = 0; i < rows; ++i)
		for (size_t j = 0; j < cols; ++j)
			data[i][j] = m[i][j];

	return *this;
}

Matrix Matrix::operator*(const int& k) const
{
	Matrix self = *this;
	for (size_t i = 0; i < rows; ++i)
		for (size_t j = 0; j < cols; ++j)
			self[i][j] = data[i][j]*k;
	return self;
}

Matrix Matrix::operator*=(const int& k)
{
	for (size_t i = 0; i < rows; ++i)
		for (size_t j = 0; j < cols; ++j)
			data[i][j] *= k;
	return *this;
}

Matrix Matrix::operator*(const Matrix& m) const
{
	if (cols != m.getRows())
		throw std::out_of_range("wrong matrixs sizes for multiply");

	Matrix res(rows, m.getColumns());

	for(size_t i = 0; i < res.getRows(); ++i)
		for(size_t j = 0; j < res.getColumns(); ++j)
			for(size_t k = 0; k < cols; ++k)
				res[i][j] += data[i][k] * m[k][j];
	return res;
}